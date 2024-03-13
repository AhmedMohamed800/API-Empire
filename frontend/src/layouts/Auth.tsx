import React from "react";
import { Outlet } from "react-router-dom";
import { useEffect } from "react";
import Cookies from "js-cookie";
import { useNavigate } from "react-router-dom";
const code_testing = require("../assets/auth/code_testing.svg") as string;
const letter_a = require("../assets/auth/letter_a.svg") as string;

function Auth() {
  const navigate = useNavigate();

  useEffect(() => {
    const session = Cookies.get("session");
    if (session) {
      navigate("/APIs");
    }
  }, []);

  return (
    <main className=" flex h-screen  ">
      <section className="relative flex w-[50%] items-center justify-center overflow-hidden bg-primary max-lg:hidden">
        <img
          src={letter_a}
          alt="letter_a1"
          className="absolute -right-[50px] -top-[10px] rotate-[0deg]"
          width="70.98px"
          height="74"
        />
        <img src={code_testing} alt="code_testing" />
        <img
          src={letter_a}
          alt="letter_a2"
          className="absolute -bottom-10 -right-10 rotate-[45deg]"
          width="70.98px"
          height="74"
        />
      </section>
      <Outlet />
    </main>
  );
}

export default Auth;
