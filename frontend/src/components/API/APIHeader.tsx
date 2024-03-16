import React from "react";

const APIHeader = ({ headerOpen }) => {
  return (
    <div className={`flex flex-col ${headerOpen || "hidden"}`}>
      <div>
        <h2 className=" rounded-t-md bg-black p-4 font-semibold">Parameters</h2>
        <section className=" bg-primary p-4 [&>div]:flex [&>div]:gap-20 ">
          <div className=" gap-20 border-b-2 border-white pb-2">
            <h3 className="w-[30px]">Name</h3>
            <h3 className="grow">Description</h3>
          </div>
          <div className="  pt-2">
            <p className="w-[30px]">Body</p>
            <div>
              <p>Elements</p>
            </div>
          </div>
        </section>
      </div>
      <div>
        <h2 className="rounded-t-md  bg-black p-4 font-semibold">Responses</h2>
        <section className="rounded-b-md bg-primary p-4 [&>div]:flex [&>div]:gap-20">
          <div className=" gap-20 border-b-2 border-white pb-2">
            <h3 className="w-[30px]">Code</h3>
            <h3 className="grow">Description</h3>
          </div>
          <div className="  pt-2">
            <p className="w-[30px]">200</p>
            <div>
              <p>Elements</p>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
};

export default APIHeader;
