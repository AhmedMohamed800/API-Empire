import React from "react";
import { useEffect } from "react";

const Traffic = () => {
  useEffect(() => {
    const TRAFFICURL = `${process.env.REACT_APP_API_URL}`;
  }, []);

  return (
    <section className="z-10 mx-20 flex grow  flex-col   justify-center gap-6 max-sm:mx-5">
      Traffic
    </section>
  );
};

export default Traffic;
