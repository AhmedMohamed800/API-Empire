import React from "react";

type Props = {
  who: string;
  type: string;
  description: string;
  cost: string;
  features: string[];
};

const Price = ({ who, type, description, cost, features }: Props) => {
  return <div>Price</div>;
};
