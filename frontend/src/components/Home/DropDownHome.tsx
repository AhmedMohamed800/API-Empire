import React from "react";
import { NavLink } from "react-router-dom";
type Props = {
  Dropdown: boolean;
  setIsOpen: (isOpen: boolean) => void;
};

const DropDownHome: React.FC<Props> = ({ Dropdown, setIsOpen }) => {
  function Close() {
    setIsOpen(false);
  }

  return (
    <div
      onClick={Close}
      className={`${Dropdown ? "block" : "hidden"} absolute right-10 top-14 z-50 flex  w-44 flex-col gap-2   rounded-sm bg-black text-center  lg:hidden [&>a:hover]:opacity-80 [&>a]:rounded-sm [&>a]:px-2 [&>a]:py-3 [&>a]:text-[16px]`}
    >
      <NavLink
        to="/"
        className={({ isActive }) => (isActive ? "bg-primary" : "")}
      >
        Home
      </NavLink>
      <NavLink
        to="/aboutus"
        className={({ isActive }) => (isActive ? "bg-primary" : "")}
      >
        About Us
      </NavLink>
      <NavLink
        to="/apihub"
        className={({ isActive }) => (isActive ? "bg-primary" : "")}
      >
        APIs
      </NavLink>
      <NavLink
        to="/pricing"
        className={({ isActive }) => (isActive ? "bg-primary" : "")}
      >
        Pricing
      </NavLink>
      <NavLink
        to="/auth/sign_in"
        className={({ isActive }) => (isActive ? "bg-primary" : "")}
      >
        Sign in
      </NavLink>
      <NavLink
        to="/auth/sign_up"
        className={({ isActive }) => (isActive ? "bg-primary" : "")}
      >
        Sign up
      </NavLink>
    </div>
  );
};

export default DropDownHome;
