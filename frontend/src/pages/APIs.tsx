import React from "react";
const arrow = require("../assets/apis/arrow.svg") as string;
import { usePaginatedAPIs } from "../components/APIs/APIsHook.tsx";
import { useState } from "react";
const search = require("../assets/apis/search.svg") as string;
const filter = require("../assets/apis/filter.svg") as string;

export const APIs = () => {
  const apisPerPage = 20;
  const [filterModel, setfilterModel] = useState<boolean>(true);
  const {
    computedApis,
    paginate,
    topRef,
    page,
    filteredApis,
    generateUUID,
    setSearchTerm,
    setSelectedCategory,
    selectedCategory,
    searchTerm,
    Categories,
  } = usePaginatedAPIs(apisPerPage);

  return (
    <div className="z-10 flex flex-col  max-sm:mx-5 ">
      <header
        className={`flex h-16 items-center justify-between gap-2 border-b-2 border-white px-20 max-sm:px-0 ${filterModel && "mb-10"}`}
      >
        <div className="flex grow gap-2">
          <img src={search} alt="search" width="24px" height="24px" />
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Search for your API..."
            className="h-10 grow bg-transparent focus:border-none focus:outline-none"
          />
        </div>
        <img
          src={filter}
          alt="filter"
          width="24px"
          height="24px"
          className="cursor-pointer"
          onClick={() => setfilterModel(!filterModel)}
        />
      </header>
      <ul
        className={`mb-6 flex min-h-24 items-center justify-center gap-2 bg-primary p-3 max-sm:flex-col ${filterModel && "hidden"}`}
      >
        {Categories.length > 0 &&
          Categories.map((cat) => {
            return (
              <li
                key={cat}
                data-category={cat}
                className={`
                  ${selectedCategory === cat ? "search_active" : "search_inactive"} capitalize
               `}
                onClick={(e) => {
                  const target = e.target as HTMLElement;
                  setSelectedCategory(target.dataset.category as string);
                  paginate(1);
                }}
              >
                {cat}
              </li>
            );
          })}
      </ul>
      <main
        ref={topRef}
        className={`mx-20 mb-6 grid grow grid-cols-1  grid-rows-1 items-center gap-5 max-sm:mx-0  ${computedApis.length > 0 && "md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5"}`}
      >
        {computedApis.length > 0 ? (
          computedApis
        ) : (
          <h1 className="order-3 text-center text-3xl ">
            THERE IS NO API HERE!
          </h1>
        )}
      </main>
      <section
        className={`mx-20 mb-10 flex flex-row-reverse items-center justify-between gap-5 max-sm:flex-col-reverse ${computedApis.length > 0 || "hidden"}`}
      >
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
              if (page < Math.ceil(filteredApis / 20)) {
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
        <div className=" flex gap-2">
          {[...Array(Math.ceil(filteredApis / 20)).keys()].map((_, index) => {
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
