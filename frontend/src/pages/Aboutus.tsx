import React from "react";
const pattern = require("../assets/landing/grid.svg") as string;
import ProfileCard from "../components/Home/ProfileCard.tsx";
const DinamowPhoto = require("../assets/landing/Dinamow.png") as string;
const AhmedPhoto = require("../assets/landing/Ahmed.png") as string;
type Props = {};

const Aboutus = (props: Props) => {
  return (
    <div className="relative mb-10">
      <div className=" relative  flex h-[400px] items-center justify-center  bg-primary  p-4 text-center">
        <h1 className="relative  w-[1000px] text-4xl font-bold max-lg:w-full max-sm:text-2xl">
          API Empire is platform that provides various APIs for developers
          through subscription-based services.
        </h1>

        <span
          style={{ background: `url(${pattern})` }}
          className="fade-effect absolute h-full w-full bg-repeat-x"
        ></span>
      </div>
      <h2 className="my-10 text-center text-4xl font-bold max-sm:text-2xl">
        Team Members
      </h2>
      <main className="mx-20 flex justify-center gap-4 max-lg:flex-col max-lg:items-center max-sm:mx-5 ">
        <ProfileCard
          name="Ahmed Mohamed"
          position="Full Stack developer"
          description="A passionate full stack developer with two years of experience in building websites and web applications using ReactJS, Tailwindcss, HTML, CSS, Javascript, Pug, ExpressJS, htmx, MySQL and MongoDB."
          email="ahmedmoh0107@gmail.com"
          github="https://github.com/AhmedMohamed800/"
          personalWebsite="https://www.linkedin.com/in/ahmed-mohamed-1a29b01ba/"
          image={AhmedPhoto}
        />
        <ProfileCard
          name="Abdou Dinamow"
          position="Backend developer"
          description="A passionate back-end developer with one year of experience in building websites and web applications using Flask, MySQL, NodeJS, MongoDB and Radis."
          email="meemoo102039@gmail.com"
          github="https://github.com/Dinamow"
          personalWebsite="https://www.linkedin.com/in/abdelrhman-mohammed-86095a19b/"
          image={DinamowPhoto}
        />
      </main>
    </div>
  );
};

export default Aboutus;
