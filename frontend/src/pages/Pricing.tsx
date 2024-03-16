import React, { useEffect, useRef } from "react";
import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js";
import axios from "axios";

type Props = {};

const Pricing = (props: Props) => {
  const paypal = useRef(null);

  return (
    <div className="relative flex flex-col  items-center  justify-center gap-6 ">
      <button className=" rounded-md bg-primary px-4 py-2 text-white hover:opacity-80">
        Buy Cock
      </button>
      <div id="paypal" ref={paypal}></div>
      <PayPalButtons />
    </div>
  );
};

export default Pricing;
