import React from "react";
import { NavLink } from "react-router-dom";
const logo = require("../../assets/logo.svg") as string;
import { useLocation } from "react-router-dom";

type Props = {};

const NavnarHome = (props: Props) => {
  const { pathname } = useLocation();
  console.log(pathname);
  return (
    <nav
      className={`z-10 flex items-center justify-between ${pathname.includes("/apihub") && "border-b border-neutral-400"} px-20 py-4`}
    >
      <NavLink to="/" className="w-[200px]">
        <img src={logo} alt="logoLanding" width="50px" height="50px" />
      </NavLink>
      <div className="flex gap-6 font-semibold [&>a:hover]:opacity-80">
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
      <div className="flex w-[160px] items-center  gap-3 font-semibold [&>a:hover]:opacity-80">
        <NavLink to="/auth/sign_in" className="">
          Sing in
        </NavLink>
        <NavLink to="/auth/sign_up" className="rounded-md bg-primary px-4 py-2">
          Join US
        </NavLink>
      </div>
    </nav>
  );
};

export default NavnarHome;
