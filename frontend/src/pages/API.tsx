import React from "react";
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from "axios";
import Endpoint from "../components/API/Endpoint.tsx";

interface APIProps {
  api_id: number;
  category: string;
  description: string;
  id: number;
  method: string;
  response_ex: string;
  title: string;
  url: string;
}

const API = () => {
  const [endpoints, setEndpoints] = useState<APIProps[]>([]);
  const [baseURL, setBaseURL] = useState<string>("");
  const { id } = useParams();

  useEffect(() => {
    const URL = `${process.env.REACT_APP_API_URL}/api/v1/service/${id}`;
    axios.get(URL).then((response) => {
      setEndpoints(response.data);
      setBaseURL(response.data[0].url);
    });
    document.title = "API";
  }, []);

  return (
    <section className="z-10 mx-20 my-10 flex flex-col gap-6 max-sm:mx-5">
      <header
        className="flex items-center gap-6 rounded-md border-2 border-primary p-4 max-sm:flex-col"
        style={{
          background:
            "linear-gradient(180deg, rgba(99, 91, 255, 0.00) 0%, rgba(99, 91, 255, 0.50) 100%)",
        }}
      >
        <div className=" flex w-80 flex-col  max-sm:w-full max-sm:text-center">
          <h1 className=" gap-2 text-3xl font-bold capitalize text-primary">
            {endpoints[endpoints.length - 1] &&
              endpoints[endpoints.length - 1]["title"]}
          </h1>
          <p className=" text-[14px] text-neutral-400">
            [ Base URL: {baseURL && new URL(baseURL).origin} ]
          </p>
        </div>
        <p className=" text-justify text-[18px]">
          {endpoints[endpoints.length - 1] &&
            endpoints[endpoints.length - 1]["description"]}
        </p>
      </header>
      <div className="rounded-md bg-post p-4 text-center text-black">
        <p>Please ensure to include the following in your headers:</p>
        <p>
          <code>X-APIEMPIR-KEY: [Your API Key]</code>
        </p>
      </div>
      <main className=" flex flex-col gap-4  border-t-2 border-white pt-6">
        {endpoints.length > 0 &&
          endpoints.map((ele, i) => {
            if (i === endpoints.length - 1) return null;

            return (
              <Endpoint
                key={ele.url}
                id={ele.id}
                title={ele.title}
                description={ele.description}
                method={ele.method}
                url={ele.url}
                response_ex={ele.response_ex}
                category={ele.category}
                base={baseURL && new URL(baseURL).origin}
              />
            );
          })}
      </main>
    </section>
  );
};

export default API;
