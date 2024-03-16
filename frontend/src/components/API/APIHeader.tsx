import React from "react";
import CustomJSONViewer from "./CustomJSONViewer.tsx";

const APIHeader = ({ headerOpen, queries, response }) => {
  return (
    <div className={`flex flex-col ${headerOpen || "hidden"}`}>
      <div>
        <h2 className=" rounded-t-md bg-black p-4 font-semibold">Parameters</h2>
        <section className=" bg-primary p-4 [&>div]:flex [&>div]:gap-20 ">
          <div className=" gap-20 border-b-2 border-white pb-2">
            <h3 className="table_api">Name</h3>
            <h3 className="table_api">value</h3>
            <h3 className="table_api">type</h3>
            <h3 className="table_api">location</h3>
          </div>
          {Array.from(queries.entries()).map(([key, value]) => {
            return (
              <div key={key} className="pt-2">
                <p className="table_api">{key}</p>
                <p className="table_api">{value}</p>
                <p className="table_api">{typeof value}</p>
                <p className="table_api">query</p>
              </div>
            );
          })}
        </section>
      </div>
      <div className="">
        <h2 className="rounded-t-md  bg-black p-4 font-semibold">Responses</h2>
        <section className="rounded-b-md bg-primary p-4 [&>div]:flex [&>div]:gap-20">
          <div className=" gap-20 border-b-2 border-white pb-2">
            <h3 className="w-[30px]">Code</h3>
            <h3 className="grow">Description</h3>
          </div>
          <div className="pt-2">
            <p className="w-[30px]">200</p>
            <code className="grow rounded-md bg-[#333333] p-4">
              {<CustomJSONViewer data={response} />}
            </code>
          </div>
          <div className="  pt-2">
            <p className="w-[30px] ">400</p>
            <p className="text-red-500">Invalid Request</p>
          </div>
          <div className="pt-2">
            <p className="w-[30px] ">404</p>
            <p className="text-red-500">Not Autherized</p>
          </div>
        </section>
      </div>
    </div>
  );
};

export default APIHeader;
