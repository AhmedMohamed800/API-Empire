import React from "react";
import { useEffect, useState, useMemo, useRef } from "react";
import APICard from "../components/APIs/APICard.tsx";
import axios from "axios";
const arrow = require("../assets/apis/arrow.svg") as string;

interface APICardProps {
  title: string;
  description: string;
  image_cover: string;
  id: string;
  category: string;
}

export const APIs = () => {
  const [apis, setApis] = useState<APICardProps[]>([]);
  const [page, setPage] = useState<number>(1);
  const topRef = useRef(null);
  const apisPerPage = 20;

  const paginate = (pageNumber) => {
    setPage(pageNumber);
    const url = new URL(window.location.href);
    url.searchParams.set("page", pageNumber);
    window.history.replaceState({}, "", url);
  };

  useEffect(() => {
    paginate(1);
    document.title = "APIs";
    const APIsURL = `${process.env.REACT_APP_API_URL}/api/v1/service/all`;
    if (sessionStorage.getItem("apis")) {
      const parsedApis = JSON.parse(sessionStorage.getItem("apis") || "");
      if (parsedApis) {
        setApis(parsedApis);
        return;
      }
    }
    axios
      .get(APIsURL)
      .then((response) => {
        sessionStorage.setItem("apis", JSON.stringify(response.data.message));
        setApis(response.data.message);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  const computedApis = useMemo(() => {
    if (apis && Array.isArray(apis) && apis.length > 0) {
      const startIndex = (page - 1) * apisPerPage;
      const endIndex = startIndex + apisPerPage;
      const apisForPage = apis.slice(startIndex, endIndex);

      return apisForPage.map((api, _) => {
        return (
          <APICard
            key={api.id}
            title={api.title}
            description={api.description}
            image_cover={api.image_cover}
            url={api.id}
            category={api.category}
          />
        );
      });
    }
    return null;
  }, [apis, page]);

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

  return (
    <div className="z-10 mx-20 my-10 grid gap-6 max-sm:mx-5 ">
      <main
        ref={topRef}
        className="grid grid-cols-1 gap-5 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
      >
        {computedApis}
      </main>
      <section className="flex flex-row-reverse items-center justify-between">
        <div className="flex gap-3">
          <button
            className="rounded-full border border-white p-2"
            onClick={() => {
              if (page > 1) {
                paginate(page - 1);
                (topRef.current as HTMLElement | null)?.scrollIntoView({
                  behavior: "smooth",
                });
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
              if (page < Math.ceil(apis.length / 20)) {
                paginate(page + 1);
                (topRef.current as HTMLElement | null)?.scrollIntoView({
                  behavior: "smooth",
                });
              }
            }}
          >
            <img src={arrow} alt="arrow-right" width="24px" height="24px" />
          </button>
        </div>
        <div className="flex gap-2">
          {[...Array(Math.ceil(apis.length / 20)).keys()].map((_, index) => {
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
          })}
        </div>
      </section>
    </div>
  );
};

export default APIs;
