import React from "react";
const logo = require("../../assets/logo.svg") as string;
import { useContext } from "react";
import { UserContext } from "../Auth/AuthHook.tsx";
import { useState } from "react";
import NavDrop from "./NavDrop.tsx";
import default_photo from "../../assets/application/default_photo.jpeg";

const NavbarApp = () => {
  const [Dropdown, setDropdown] = useState<boolean>(true);
  const user = useContext(UserContext);

  return (
    <nav className="border- relative  flex justify-between  border-b border-neutral-400 px-20 py-2">
      <img src={logo} alt="logo3" />
      <div
        onClick={() => {
          setDropdown(!Dropdown);
        }}
        className="relative flex cursor-pointer select-none flex-row-reverse items-center gap-2"
      >
        <div
          id="photo"
          className=" bg-cotain h-12 w-12 rounded-full border-2 border-primary "
          style={{ backgroundImage: `url(${default_photo})` }}
        ></div>
        <div className="text-right">
          <p className=" text-[16px] text-primary">
            {user.first_name} {user.last_name}
          </p>
          <p className=" text-[14px] text-neutral-400">Open your profile</p>
        </div>
        <NavDrop Dropdown={Dropdown} setDropdown={setDropdown} />
      </div>
    </nav>
  );
};

export default NavbarApp;
