import React from "react";
import { NavLink } from "react-router-dom";
import Cookies from "js-cookie";
import axios from "axios";
import { useNavigate } from "react-router-dom";

interface NavDropProps {
  Dropdown: boolean;
  setDropdown: React.Dispatch<React.SetStateAction<boolean>>;
}

const NavDrop = ({ Dropdown, setDropdown }: NavDropProps) => {
  const navigate = useNavigate();

  function logout() {
    axios
      .delete(`${process.env.REACT_APP_API_URL}/api/v1/login`, {
        headers: {
          "session-id": JSON.parse(Cookies.get("session")),
        },
      })
      .then(() => {
        Cookies.remove("session");
        navigate("/auth/sign_in");
      })
      .catch((error) => {
        Cookies.remove("session");
        navigate("/auth/sign_in");
        console.log(error);
      });
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
      <button
        onClick={logout}
        className="px-2 py-3 text-[16px] hover:opacity-80"
      >
        Logout
      </button>
    </div>
  );
};

export default NavDrop;
