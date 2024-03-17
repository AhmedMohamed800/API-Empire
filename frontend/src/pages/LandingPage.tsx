import React from "react";
import { useEffect } from "react";
import { NavLink } from "react-router-dom";

type Props = {};

const LandingPage = (props: Props) => {
  useEffect(() => {
    document.title = "Home | API Empire";
  }, []);
  return (
    <div className="z-10 mx-20 mb-10 mt-14 flex flex-col gap-16 max-sm:mx-5">
      <header className="flex flex-col items-center justify-center gap-4 text-center ">
        <h1 className="  w-[800px]  text-6xl font-bold">
          API Empire is a{" "}
          <span className="underline-primary text-primary underline">
            better
          </span>{" "}
          way to build products
        </h1>
        <p className="w-[500px] text-[18px] text-neutral-400">
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
      <section className="h-[580.88px] bg-white"></section>
      <section>
        <h4>TRUSTED BY THE INDUSTRY LEADERS</h4>
        <div></div>
      </section>
      <main>
        <img src="" alt="" />
        <div>
          <h4>Unlock Innovation with Diverse API Toolkit</h4>
          <p>
            Access a diverse range of APIs covering crucial functionalities such
            as Social Media, Natural Language Processing, Image Recognition, and
            more.
          </p>
        </div>
      </main>
      <section>
        <h5>Ready to get started?</h5>
        <p>Create an account or discover our APIs</p>
        <div>
          <NavLink to="sign_in">Get Started</NavLink>
          <NavLink to="/apihub">Explore APIs</NavLink>
        </div>
      </section>
    </div>
  );
};

export default LandingPage;
