import React, { useEffect, useState } from "react";
import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js";
import { useLocation, useNavigate } from "react-router-dom";
import axios from "axios";
import Cookies from "js-cookie";

interface paymentInfo {
  price: number;
  request: number;
}

const Checkout = () => {
  const location = useLocation();
  const navigate = useNavigate();

  const [paymentInfo, setPaymentInfo] = useState<paymentInfo>({
    price: 0,
    request: 0,
  });

  const initialOptions = {
    clientId: `${process.env.REACT_APP_PAYPAL_CLIENT_ID}`,
    currency: "USD",
    intent: "capture",
  };
  const { price, request } = location.state;

  useEffect(() => {
    if (!location.state) {
      navigate("/billing");
    } else {
      setPaymentInfo((prev) => ({ ...prev, price, request }));
    }
  }, []);

  const createOrder = (data, actions) => {
    const CreatePaymentURL = `${process.env.REACT_APP_API_URL}/api/v1/payment/create`;
    return axios
      .post(CreatePaymentURL, {
        name: "Requests Purchase",
        sku: 1,
        price: price,
        currency: "USD",
      })
      .then((response) => {
        return response.data;
      })
      .then((order) => {
        return order.id;
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const onApprove = (data, actions) => {
    return actions.order.capture().then((details) => {
      const CreatePaymentURL = `${process.env.REACT_APP_API_URL}/api/v1/payment/execute`;
      console.log(details);

      const session = Cookies.get("session");
      if (session) {
        axios
          .post(
            CreatePaymentURL,
            {
              paymentID: details.id,
              amount: price,
            },
            { headers: { "session-id": JSON.parse(session) } },
          )
          .then((res) => {
            navigate("/billing");
          })
          .catch((e) => {
            console.log(e);
          });
      }
    });
  };

  const onError = (err) => {
    return false;
  };

  return (
    <PayPalScriptProvider options={initialOptions}>
      <div className=" z-10 mx-auto  flex w-[550px] flex-col justify-center gap-4  max-sm:w-full max-sm:px-4 ">
        <section className="rounded-md bg-primary p-4">
          <div className="mb-2 flex justify-between text-[18px]">
            <p>API Empire</p>
          </div>

          <p className="text-3xl">{paymentInfo.price}$</p>
          <p>Requests: {paymentInfo.request}</p>
        </section>

        <PayPalButtons
          createOrder={createOrder}
          onApprove={onApprove}
          onError={onError}
        />
      </div>
    </PayPalScriptProvider>
  );
};

export default Checkout;
