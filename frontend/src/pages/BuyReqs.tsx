import React from "react";
import { useEffect, useState } from "react";
const arrow = require("../assets/payment/arrow.svg") as string;
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

type Props = {};

const BuyReqs = (props: Props) => {
  const [price, setPrice] = useState(1);
  const navigate = useNavigate();
  const { pathname } = useLocation();

  function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
    if (parseInt(event.target.value) > 50000000) return setPrice(50000000);

    setPrice((price) => {
      return parseInt(event.target.value);
    });
  }

  function getPaymentID(e) {
    if (price === 0 || isNaN(price)) return;
    if (pathname.includes("/pricing")) {
      navigate("/billing");
    } else {
      navigate(`/checkout`, {
        state: {
          price: (price * 0.01).toFixed(2),
          request: price,
        },
      });
    }
  }

  return (
    <div className="z-10 mx-20 mb-10 mt-14 flex flex-col gap-20 max-sm:mx-5">
      <header className={`flex flex-col gap-5 `}>
        <p className="text-center text-[18px] font-semibold leading-4 text-primary">
          PRICING
        </p>
        <h1 className="text-center text-4xl font-semibold text-white">
          Transparent, Flexible, Affordable
        </h1>
      </header>
      <main
        className={`mx-auto flex w-[800px] flex-col gap-6 max-lg:w-[500px] max-sm:w-full `}
      >
        <div className="self-center rounded-md bg-primary px-6 py-3 text-center">
          <h4>Estimated Cost</h4>
          <p>{price ? (price * 0.01).toFixed(2) : 0}$</p>
        </div>
        <div className="flex flex-col gap-6">
          <label
            htmlFor="price"
            className="flex  items-center justify-center gap-6"
          >
            <span className="rounded-md bg-primary px-4 py-[10px]">
              Requests
            </span>
            <input
              type="number"
              id="price"
              name="price"
              min={1}
              max={50000000}
              value={price ? price : ""}
              onChange={handleChange}
              className="w-full rounded-md border-2 border-white bg-transparent px-4 py-2 text-white focus:outline-none"
            />
          </label>
          <section className="flex justify-between max-sm:flex-col max-sm:items-center">
            <div className="flex gap-6">
              <button className="flex flex-col items-center gap-2">
                <img
                  src={arrow}
                  alt="Substract 100"
                  className="rotate-180 rounded-md bg-primary px-4 py-3 hover:opacity-80"
                  onClick={() => {
                    setPrice((price) => {
                      if (!(price - 100 < 0)) {
                        return price - 100;
                      }
                      return 0;
                    });
                  }}
                />
                <p className="text-[18px]">-100</p>
              </button>
              <button className="flex flex-col items-center gap-2">
                <img
                  src={arrow}
                  alt="Substract 10"
                  className="rotate-180 rounded-md bg-primary px-4 py-3 hover:opacity-80"
                  onClick={() => {
                    setPrice((price) => {
                      if (!(price - 10 < 0)) {
                        return price - 10;
                      }
                      return 0;
                    });
                  }}
                />
                <p className="text-[18px]">-10</p>
              </button>
              <button className="flex flex-col items-center gap-2">
                <img
                  src={arrow}
                  alt="Substract one"
                  className="rotate-180 rounded-md bg-primary px-4 py-3 hover:opacity-80"
                  onClick={() => {
                    setPrice((price) => {
                      if (!(price - 1 < 0)) {
                        return price - 1;
                      }
                      return 0;
                    });
                  }}
                />
                <p className="text-[18px]">-1</p>
              </button>
            </div>
            <div className="flex gap-4">
              <button className="flex flex-col items-center gap-2">
                <img
                  src={arrow}
                  alt="Add one"
                  className=" rounded-md bg-primary px-4 py-3 hover:opacity-80"
                  onClick={() => {
                    setPrice((price) => {
                      if (!(price + 100 > 50000000)) {
                        return price + 100;
                      }
                      return 50000000;
                    });
                  }}
                />
                <p className="text-[18px]">+100</p>
              </button>
              <button className="flex flex-col items-center gap-2">
                <img
                  src={arrow}
                  alt="Add 10"
                  className=" rounded-md bg-primary px-4 py-3 hover:opacity-80"
                  onClick={() => {
                    setPrice((price) => {
                      if (!(price + 10 > 50000000)) {
                        return price + 10;
                      }
                      return 50000000;
                    });
                  }}
                />
                <p className="text-[18px]">+10</p>
              </button>
              <button className="flex flex-col items-center gap-2">
                <img
                  src={arrow}
                  alt="Add 1"
                  className="rounded-md bg-primary px-4 py-3 hover:opacity-80"
                  onClick={() => {
                    setPrice((price) => {
                      if (!(price + 1 > 50000000)) {
                        return price + 1;
                      }
                      return 50000000;
                    });
                  }}
                />
                <p className="text-[18px]">+1</p>
              </button>
            </div>
          </section>
        </div>
        <button
          className=" self-center rounded-md bg-primary px-6 py-3 hover:opacity-80"
          onClick={getPaymentID}
        >
          {pathname.includes("/pricing") ? "Join Us" : "Pay Now"}
        </button>
      </main>
    </div>
  );
};

export default BuyReqs;
