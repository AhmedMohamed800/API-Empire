import React from "react";
import { useParams } from "react-router-dom";

const API = () => {
  const { id } = useParams();

  return <div>{id}</div>;
};

export default API;
