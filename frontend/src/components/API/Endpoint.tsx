import React from "react";
import APIHeader from "./APIHeader.tsx";
import { useState } from "react";
interface EndpointProps {
  id: number;
  title: string;
  description: string;
  method: string;
  url: string;
  response_ex: string;
  category: string;
  base: string;
}

const Endpoint: React.FC<EndpointProps> = ({
  id,
  title,
  description,
  method,
  url,
  response_ex,
  category,
  base,
}) => {
  const restURL = new URL(url);
  const queries = restURL.searchParams;
  const [headerOpen, setHeaderOpen] = useState(false);
  const responseWithQuotation = response_ex.replace(/'/gi, '"');
  let backgroundColor;
  if (method === "GET") {
    backgroundColor =
      "linear-gradient(180deg, rgba(99, 91, 255, 0.00) 0%, rgba(99, 91, 255, 0.50) 100%)";
  } else if (method === "POST") {
    backgroundColor =
      "linear-gradient(180deg, rgba(242, 255, 91, 0.00) 0%, rgba(242, 255, 91, 0.50) 100%)";
  }

  return (
    <>
      <div
        style={{ background: backgroundColor }}
        className={`${method === "GET" ? "border-primary" : "border-post"} flex w-full cursor-pointer  items-center gap-4 rounded-md border-2 p-4`}
        onClick={(e) => {
          if (
            e.target instanceof HTMLElement &&
            !(e.target.tagName === "BUTTON")
          ) {
            setHeaderOpen(!headerOpen);
          }
        }}
      >
        <p
          className={`${method === "GET" ? "bg-primary" : "bg-post text-black"} rounded-md px-4 py-[3px] font-semibold uppercase`}
        >
          {method}
        </p>
        <p className="relative grow font-semibold">
          {restURL.pathname}
          <button
            className=" mb-2 ml-4 rounded-md bg-primary px-2 py-[1px] hover:opacity-80 max-sm:absolute max-sm:-left-[94px] max-sm:bottom-10"
            onClick={() => {
              const URL = `${base}${restURL.pathname}${restURL.search}`;
              navigator.clipboard
                .writeText(URL)
                .then(() => {
                  alert("URL copied to clipboard");
                })
                .catch((err) => {
                  console.error("Could not copy text: ", err);
                });
            }}
          >
            Copy
          </button>

          <span
            className="overflow-hidden  text-sm text-neutral-300"
            style={{
              display: "-webkit-box",
              WebkitLineClamp: 1,
              WebkitBoxOrient: "vertical",
              maxWidth: "200ch",
            }}
          >
            {description}
          </span>
        </p>
        <svg
          width="20"
          height="22"
          viewBox="0 0 18 20"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className={`${headerOpen && "rotate-180"} h-[22px] w-[20px] transition-transform duration-300 ease-in-out`}
        >
          <g id="icon">
            <path
              id="icon_2"
              d="M5.25 8.33334L9 12.5L12.75 8.33334L5.25 8.33334Z"
              fill="#F2FF5B"
              className={`${method === "GET" ? "fill-primary" : "fill-post"}`}
            />
          </g>
        </svg>
      </div>
      <APIHeader
        headerOpen={headerOpen}
        queries={queries}
        response={JSON.parse(responseWithQuotation)}
      />
    </>
  );
};

export default Endpoint;
