import React from "react";
import { Link } from "react-router-dom";

type Props = {};

const NotFound = (props: Props) => {
  return (
    <div className="relative flex h-screen flex-col items-center justify-center gap-6 bg-black">
      <h1 className="text-4xl font-bold">This Page Doesn't Exist</h1>
      <div className="flex items-center gap-4 [&>a:hover]:opacity-80">
        <Link to="/" className="rounded-md bg-primary px-4 py-2">
          Back Home
        </Link>
        <a
          className="rounded-md bg-primary px-4 py-2"
          href="https://www.youtube.com/watch?v=9VC_5Cxg1NM&ab_channel=FunnyAndCuteCat%27sLife"
        >
          ≽^•⩊•^≼ Cat Videos
        </a>
        <a
          className="rounded-md bg-primary px-4 py-2"
          href="https://www.youtube.com/watch?v=t99MQo9voVk&pp=ygUKRG9nIFZpZGVvcw%3D%3D"
        >
          ≽^•⩊•^≼ Dog Videos
        </a>
      </div>
      <div className=" absolute -right-10 bottom-0 h-56 w-56 rounded-full bg-primary blur-[160px]"></div>
      <div className=" absolute -left-10 top-0    h-56 w-56 rounded-full bg-primary blur-[160px]"></div>
    </div>
  );
};

export default NotFound;
