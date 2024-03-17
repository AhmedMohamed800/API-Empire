import React from "react";
import { useEffect, useState, useMemo } from "react";
import axios from "axios";
import Cookies from "js-cookie";
import Table from "../components/Application/Table.tsx";
const arrow = require("../assets/apis/arrow.svg") as string;

const Traffic = () => {
  const paginate = (pageNumber) => {
    setPage(pageNumber);
    const url = new URL(window.location.href);
    url.searchParams.set("page", pageNumber);
    window.history.replaceState({}, "", url);
  };

  function generateUUID() {
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(
      /[xy]/g,
      function (c) {
        var r = (Math.random() * 16) | 0,
          v = c === "x" ? r : (r & 0x3) | 0x8;
        return v.toString(16);
      },
    );
  }
  const [traffic, setTrafic] = useState([]);
  const [page, setPage] = useState(1);
  const apisPerPage = 7;

  const header = ["ip", "date", "method", "url", "status"];
  useEffect(() => {
    const url = new URL(window.location.href);
    const page = url.searchParams.get("page");
    if (page) {
      setPage(parseInt(page));
    } else {
      paginate(1);
    }
    document.title = "Traffic";

    const session = Cookies.get("session");
    const TRAFFICURL = `${process.env.REACT_APP_API_URL}/api/v1/get_reqs`;

    axios
      .get(TRAFFICURL, { headers: { "session-id": JSON.parse(session) } })
      .then((res) => {
        const updatedData = res.data.map((item) => ({
          ...item,
          url: item.path,
          status: item.status_code,
        }));
        setTrafic(updatedData);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  const computedTraffic = useMemo(() => {
    const startIndex = (page - 1) * apisPerPage;
    const endIndex = startIndex + apisPerPage;
    return traffic.slice(startIndex, endIndex);
  }, [traffic, page, apisPerPage]);

  return (
    <section className="z-10 mx-20 flex grow  flex-col   justify-center gap-6 max-lg:my-10 max-sm:mx-5">
      <Table
        header={header}
        content={computedTraffic}
        generateUUID={generateUUID}
      />
      <section
        className={`  flex flex-row-reverse items-center justify-between gap-5 max-sm:flex-col-reverse ${computedTraffic.length > 0 || "hidden"}`}
      >
        <div className="flex gap-3">
          <button
            className="rounded-full border border-white p-2"
            onClick={() => {
              if (page > 1) {
                paginate(page - 1);
              }
            }}
          >
            <img
              src={arrow}
              alt="arrow-left"
              width="24px"
              height="24px"
              className=" rotate-180 "
            />
          </button>
          <button
            className="rounded-full border border-white p-2"
            onClick={() => {
              if (page < Math.ceil(traffic.length / apisPerPage)) {
                paginate(page + 1);
              }
            }}
          >
            <img src={arrow} alt="arrow-right" width="24px" height="24px" />
          </button>
        </div>
        <div className=" flex gap-2">
          {[...Array(Math.ceil(traffic.length / apisPerPage)).keys()].map(
            (_, index) => {
              const uuid = generateUUID();
              if (index === page - 1) {
                return (
                  <span
                    key={uuid}
                    className="h-2 w-2 rounded-full bg-primary"
                  ></span>
                );
              }

              return (
                <span
                  key={uuid}
                  className=" h-2 w-2 rounded-full bg-neutral-500"
                ></span>
              );
            },
          )}
        </div>
      </section>
    </section>
  );
};

export default Traffic;
