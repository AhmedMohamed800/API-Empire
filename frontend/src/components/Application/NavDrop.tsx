import React from "react";
import { NavLink } from "react-router-dom";
import Cookies from "js-cookie";

interface NavDropProps {
  Dropdown: boolean;
  setDropdown: React.Dispatch<React.SetStateAction<boolean>>;
}

const NavDrop = ({ Dropdown, setDropdown }: NavDropProps) => {
  function logout() {
    Cookies.remove("session");
  }

  return (
    <div
      className={`${Dropdown ? "block" : "hidden"} absolute right-[2px] top-16 z-20  flex w-44 flex-col   gap-2 rounded-sm bg-black  text-center [&>a:hover]:opacity-80 [&>a]:rounded-sm [&>a]:px-2 [&>a]:py-3 [&>a]:text-[16px]`}
    >
      <NavLink
        to="/APIs"
        className={({ isActive }) => (isActive ? "bg-primary" : "")}
      >
        APIs
      </NavLink>
      <NavLink
        to="/User"
        className={({ isActive }) => (isActive ? "bg-primary" : "")}
      >
        User
      </NavLink>
      <NavLink
        to="/Billing"
        className={({ isActive }) => (isActive ? "bg-primary" : "")}
      >
        Billing
      </NavLink>
      <NavLink
        to="/Traffic"
        className={({ isActive }) => (isActive ? "bg-primary" : "")}
      >
        Traffic
      </NavLink>
      <NavLink to="/auth/sign_in" onClick={logout}>
        Logout
      </NavLink>
    </div>
  );
};

export default NavDrop;
