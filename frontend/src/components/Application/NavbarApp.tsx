import React from "react";
const logo = require("../../assets/logo.svg") as string;
import { useContext } from "react";
import { UserContext } from "../Auth/AuthHook.tsx";
import { useState } from "react";
import NavDrop from "./NavDrop.tsx";
const default_photo =
  require("../../assets/application/default_photo.jpeg") as string;
import { NavLink } from "react-router-dom";
import Skeleton from "react-loading-skeleton";

const NavbarApp = () => {
  const [Dropdown, setDropdown] = useState<boolean>(false);
  const { user }: any = useContext(UserContext);
  return (
    <nav className=" relative  z-20 flex items-center  justify-between border-b border-neutral-400 px-20 py-2 max-sm:px-5">
      <NavLink to="/User">
        <img src={logo} alt="logo3" />
      </NavLink>

      <div
        onClick={() => {
          setDropdown(!Dropdown);
        }}
        className="relative flex cursor-pointer select-none flex-row-reverse items-center gap-2"
      >
        <div
          id="photo"
          className=" h-12 w-12 rounded-full border-2 border-primary  bg-cover bg-center bg-no-repeat"
          style={{ backgroundImage: `url(${default_photo})` }}
        ></div>
        <div className="text-right">
          <p className=" text-[16px] text-primary">
            {user.first_name ? (
              <>
                {user.first_name} {user.last_name}
              </>
            ) : (
              <Skeleton duration={2} />
            )}
          </p>
          <p className=" text-[14px] text-neutral-400">Open your profile</p>
        </div>
        <NavDrop Dropdown={Dropdown} setDropdown={setDropdown} />
      </div>
    </nav>
  );
};

export default NavbarApp;
