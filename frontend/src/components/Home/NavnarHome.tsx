import React from "react";
import { NavLink } from "react-router-dom";
const logo = require("../../assets/logo.svg") as string;
import { useLocation } from "react-router-dom";
import { useState } from "react";
import DropDownHome from "./DropDownHome.tsx";

type Props = {};

const NavnarHome = (props: Props) => {
  const { pathname } = useLocation();
  const [isOpen, setIsOpen] = useState(false);
  return (
    <nav
      className={`relative z-20 flex items-center justify-between  ${pathname.includes("/apihub") && "border-b border-neutral-400"} px-20 py-4`}
    >
      <NavLink to="/" className="w-[160px]">
        <img src={logo} alt="logoLanding" width="50px" height="50px" />
      </NavLink>
      <div className="flex items-center gap-6 font-semibold max-lg:hidden [&>a:hover]:opacity-80">
        <NavLink
          to="/"
          className={({ isActive }) => (isActive ? "activeHome" : "")}
        >
          Home
        </NavLink>
        <NavLink
          to="/aboutus"
          className={({ isActive }) => (isActive ? "activeHome" : "")}
        >
          About Us
        </NavLink>
        <NavLink
          to="/apihub"
          className={({ isActive }) => (isActive ? "activeHome" : "")}
        >
          APIs
        </NavLink>

        <NavLink
          to="/pricing"
          className={({ isActive }) => (isActive ? "activeHome" : "")}
        >
          Pricing
        </NavLink>
      </div>
      <div className="flex w-[160px] items-center  gap-3 font-semibold max-lg:hidden [&>a:hover]:opacity-80">
        <NavLink to="/auth/sign_in" className="">
          Sing in
        </NavLink>
        <NavLink to="/auth/sign_up" className="rounded-md bg-primary px-4 py-2">
          Join US
        </NavLink>
      </div>
      <button
        className="flex flex-col gap-1 lg:hidden"
        onClick={() => setIsOpen(!isOpen)}
      >
        <span className="h-1 w-8 rounded-full bg-white"></span>
        <span className="h-1 w-8 rounded-full bg-white"></span>
        <span className="h-1 w-8 rounded-full bg-white"></span>
      </button>

      {isOpen && <DropDownHome Dropdown={isOpen} setIsOpen={setIsOpen} />}
    </nav>
  );
};

export default NavnarHome;
