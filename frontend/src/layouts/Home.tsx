import React from "react";
import { Outlet } from "react-router-dom";
import Footer from "../components/Application/Footer.tsx";
import NavnarHome from "../components/Home/NavnarHome.tsx";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Cookies from "js-cookie";

const Home = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const session_id = Cookies.get("session");
    if (session_id) {
      navigate("/APIs");
    }
  }, []);

  return (
    <section className="relative flex max-h-full min-h-screen flex-col justify-between  text-white [&>*:nth-child(2)]:flex-grow">
      <NavnarHome />
      <Outlet />
      <Footer />

      <div className=" absolute -right-10 bottom-0 z-[1] h-56 w-56 rounded-full bg-primary blur-[160px]"></div>
      <div className=" absolute -left-10 top-0    z-[1] h-56 w-56 rounded-full bg-primary blur-[160px]"></div>
    </section>
  );
};

export default Home;
