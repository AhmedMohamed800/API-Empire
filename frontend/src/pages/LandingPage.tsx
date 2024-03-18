import React from "react";
import { useEffect } from "react";
import { NavLink } from "react-router-dom";
const apis = require("../assets/landing/apis.jpg") as string;
const globe = require("../assets/landing/globe.svg") as string;
import { Link } from "react-router-dom";
type Props = {};

const LandingPage = (props: Props) => {
  useEffect(() => {
    document.title = "Home | API Empire";
  }, []);

  return (
    <div className="realtive z-10 mx-20 mb-10 mt-14 flex flex-col gap-16 max-lg:mx-10 max-sm:mx-5">
      <header className="flex flex-col items-center justify-center gap-4 text-center ">
        <h1 className="  w-[800px]  text-6xl font-bold max-lg:w-[400px] max-lg:text-4xl max-sm:w-full max-sm:text-3xl">
          API Empire is a{" "}
          <span className="underline-primary text-primary underline">
            better
          </span>{" "}
          way to build products
        </h1>
        <p className="w-[500px] text-[18px] text-neutral-400  max-lg:w-full max-sm:text-[16px]">
          A platform that provides various APIs for developers through
          subscription-based services.
        </p>
        <NavLink
          to="/auth/sign_in"
          className=" rounded-md bg-primary px-6 py-2 text-center font-semibold text-white transition-all duration-300 ease-in-out hover:opacity-80"
        >
          Get Started
        </NavLink>
      </header>
      <section
        className="bg-cotain  relative h-[700.88px] rounded-md  bg-black bg-center bg-no-repeat max-lg:h-[500px] max-sm:h-[400px] xl:mx-20"
        style={{ backgroundImage: `url(${apis})` }}
      >
        <span className=" absolute left-0 top-0 -z-10  h-[700px] w-full bg-primary blur-[110px]"></span>
      </section>
      <section className="flex flex-col gap-4">
        <h4 className="text-center">TRUSTED BY THE INDUSTRY LEADERS</h4>
        <div className="flex items-center justify-center gap-5 max-sm:flex-col  ">
          <p className="text-xl font-semibold">Ahmed</p>
          <p className="text-xl font-semibold">Dinamow</p>
          <p className="text-xl font-semibold">Xamfra</p>
          <p className="text-xl font-semibold">Mekawy </p>
        </div>
      </section>
      <main className="flex items-center justify-evenly gap-6 max-lg:flex-col  ">
        <div className="">
          <img
            src={globe}
            alt="globe"
            width="502px"
            height="456.15px"
            className="max-lg:w-[400px]"
          />
        </div>
        <div className="flex  flex-col gap-3">
          <h4 className="text-2xl font-bold">
            Unlock Innovation with Diverse API Toolkit
          </h4>
          <p className="  mb-5 w-[500px] break-words text-justify text-neutral-400 max-sm:w-full">
            Access a diverse range of APIs covering crucial functionalities such
            as Social Media, Natural Language Processing, Image Recognition, and
            more.
          </p>
          <Link
            to="/auth/sign_up"
            className="self-start rounded-md bg-primary px-7 py-2 hover:opacity-80 max-lg:self-center"
          >
            Get Started
          </Link>
        </div>
      </main>
      <section className="flex flex-col items-center justify-center gap-4 rounded-md bg-primary px-2 py-10 text-center">
        <h5 className="text-4xl font-bold max-sm:text-2xl">
          Ready to get started?
        </h5>
        <p className="text-[16px]">Create an account or discover our APIs</p>
        <div className="flex items-center gap-3 max-sm:flex-col">
          <Link
            to="/auth/sign_in"
            className="rounded-md bg-white px-4 py-2 font-medium text-primary hover:opacity-80"
          >
            Get Started
          </Link>
          <Link to="/apihub" className="font-medium hover:opacity-80">
            Explore APIs
          </Link>
        </div>
      </section>
    </div>
  );
};

export default LandingPage;
