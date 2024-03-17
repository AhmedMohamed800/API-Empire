import React from "react";
import { useEffect, useState, useMemo } from "react";
import axios from "axios";
import Cookies from "js-cookie";
import { useNavigate } from "react-router-dom";
import Table from "../components/Application/Table.tsx";
const arrow = require("../assets/apis/arrow.svg") as string;
import { Link } from "react-router-dom";

interface Req {
  available_req: number;
  max_req: number;
  used_req: number;
}

const Billing = () => {
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

  const paginate = (pageNumber) => {
    setPage(pageNumber);
    const url = new URL(window.location.href);
    url.searchParams.set("page", pageNumber);
    window.history.replaceState({}, "", url);
  };

  const navigate = useNavigate();
  const [reqs, setReqs] = useState<Req>({
    available_req: 0,
    max_req: 0,
    used_req: 0,
  });
  const [invoices, setInvoices] = useState<any[]>([]);
  const [page, setPage] = useState(1);
  const apisPerPage = 7;
  const [noKey, Setkey] = useState<boolean>(false);
  const [totalPrice, setTotalPrice] = useState<number>(0);
  const header = ["invoice_id", "Billing Date", "amount", "requests"];

  useEffect(() => {
    const requestURL = `${process.env.REACT_APP_API_URL}/api/v1/reqs`;
    const invoiceURL = `${process.env.REACT_APP_API_URL}/api/v1/payment/all`;
    const session = Cookies.get("session");
    if (session) {
      axios
        .get(requestURL, { headers: { "session-id": JSON.parse(session) } })
        .then((res) => {
          console.log(res.data);
          if (res.data.available_req === 0) {
            navigate("/buyreqs");
          }
          setReqs(res.data);
        })
        .catch((err) => {
          Setkey(true);
        });

      axios
        .get(invoiceURL, { headers: { "session-id": JSON.parse(session) } })
        .then((res) => {
          const newData = res.data.map((item: any) => {
            setTotalPrice((prev) => prev + parseFloat(item["amount"]));
            item["invoice_id"] = "#" + item["id"];
            item["Billing Date"] = item["created_at"];
            item["requests"] = item["request"];
            item["amount"] = item["amount"] + "$";
            delete item["id"];
            delete item["created_at"];
            delete item["request"];
            return item;
          });
          setInvoices(newData);
        })
        .catch((err) => {
          console.log(err);
        });
    }
  }, []);

  const computedTraffic = useMemo(() => {
    const startIndex = (page - 1) * apisPerPage;
    const endIndex = startIndex + apisPerPage;
    return invoices.slice(startIndex, endIndex);
  }, [invoices, page, apisPerPage]);

  return (
    <div className="relative z-10 mx-20 my-10 max-lg:mx-5 ">
      <section className={`${noKey && "hidden"} mb-6 flex flex-col  gap-4`}>
        <div className="  flex items-center justify-evenly max-xl:justify-between">
          <div className="">
            <p>User Level</p>
            <p className="text-xl font-semibold">{"Giga Chad"}</p>
          </div>
          <div className="">
            <p>Total Spend</p>
            <p className="text-xl font-semibold">${totalPrice.toFixed(2)}</p>
          </div>
        </div>
        <div className="grid gap-1">
          <p>Usage</p>
          <p className="text-xl font-semibold">
            {reqs.used_req} requests out of {reqs.max_req}
          </p>
          <div className="relative h-4 rounded-full bg-white before:h-5 ">
            <span
              className="absolute left-0 top-0 h-4 rounded-s-full bg-primary"
              style={{ width: `${(reqs.used_req / reqs.max_req) * 100}%` }}
            ></span>
          </div>
        </div>
      </section>
      <section className={`${noKey && "hidden"} flex flex-col gap-4`}>
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
                if (page < Math.ceil(invoices.length / apisPerPage)) {
                  paginate(page + 1);
                }
              }}
            >
              <img src={arrow} alt="arrow-right" width="24px" height="24px" />
            </button>
          </div>
          <div className=" flex gap-2">
            {[...Array(Math.ceil(invoices.length / apisPerPage)).keys()].map(
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
        <div className="flex flex-col items-center gap-3">
          <p className="text-xl font-semibold">More Requests?</p>
          <Link
            to="/buyreqs"
            className="rounded-md bg-primary px-4  py-2 text-center hover:opacity-80"
          >
            Buy Now
          </Link>
        </div>
      </section>
      <h1
        className={`${noKey || "hidden"} absolute left-[50%] top-[50%] translate-x-[-50%] translate-y-[-50%] text-center text-5xl`}
      >
        Go to User and generate a key
      </h1>
    </div>
  );
};

export default Billing;
