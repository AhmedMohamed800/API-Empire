import React from "react";
import { useEffect } from "react";

export const APIs = () => {
  useEffect(() => {
    document.title = "APIs";
  }, []);

  return <div className="relative z-10 mx-20">APIs</div>;
};

export default APIs;
