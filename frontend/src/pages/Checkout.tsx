import React, { useEffect, useState } from "react";
import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js";
import { useLocation, useNavigate } from "react-router-dom";
import axios from "axios";

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
      setPaymentInfo({ price, request });
    }
  }, []);

  const onApprove = (data, actions) => {
    return actions.order.capture().then((details) => {
      const CreatePaymentURL = `${process.env.REACT_APP_API_URL}/api/v1/payment/execute`;
      console.log(details);
      axios
        .post(CreatePaymentURL, { paymentID: details.id })
        .then((res) => {
          console.log(res);
        })
        .catch((e) => {
          console.log(e);
        });
    });
  };

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

  return (
    <PayPalScriptProvider options={initialOptions}>
      <div className=" z-10 mx-auto  flex w-[550px] flex-col  justify-center gap-4 ">
        <section className="rounded-md bg-primary p-4">
          <div className="mb-2 flex justify-between text-[18px]">
            <p>API Empire</p>
          </div>

          <p className="text-3xl">{paymentInfo.price}$</p>
          <p>Requests: {paymentInfo.request}</p>
        </section>

        <PayPalButtons onApprove={onApprove} createOrder={createOrder} />
      </div>
    </PayPalScriptProvider>
  );
};

export default Checkout;
