import React from "react";
const gituhb = require("../../assets/landing/github.svg");
const website = require("../../assets/landing/website.svg");

type Props = {
  name: string;
  position: string;
  image: string;
  description: string;
  email: string;
  github: string;
  personalWebsite: string;
};

const ProfileCard = ({
  name,
  position,
  image,
  description,
  email,
  github,
  personalWebsite,
}: Props) => {
  return (
    <div className="coolbg flex  w-[550px] flex-col justify-between gap-3 rounded-md border-2 border-primary p-4 max-sm:w-full">
      <div className=" flex items-center gap-3">
        <div
          style={{
            backgroundImage: `url(${image})`,
          }}
          className=" h-[70px] w-[70px] rounded-full border-2 border-primary bg-cover bg-center  bg-no-repeat"
        ></div>
        <div>
          <h4 className="text-xl font-semibold">{name}</h4>
          <p className=" text-neutral-200">{position}</p>
        </div>
      </div>
      <p className=" text-justify text-primary-100">{description}</p>
      <a
        href={`https://mail.google.com/mail/u/1/?view=cm&fs=1&to=${email}&tf=1`}
        target="_blank"
        aria-label="Email"
        className="rounded-md bg-primary py-3 text-center font-semibold hover:opacity-80"
      >
        Hire me
      </a>
      <div className="flex items-center justify-center gap-2">
        <a href={github}>
          <img
            src={gituhb}
            alt={`github ${name}`}
            className="hover:opacity-80"
          />
        </a>
        <a href={personalWebsite}>
          <img
            src={website}
            alt={`website ${name}`}
            className="hover:opacity-80"
          />
        </a>
      </div>
    </div>
  );
};

export default ProfileCard;
