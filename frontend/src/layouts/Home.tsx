import React from "react";
import { Outlet } from "react-router-dom";
import Footer from "../components/Application/Footer.tsx";
import NavnarHome from "../components/Home/NavnarHome.tsx";

const Home = () => {
  return (
    <section className="relative flex max-h-full min-h-screen flex-col justify-between  text-white [&>*:nth-child(2)]:flex-grow">
      <NavnarHome />
      <Outlet />
      <Footer />
    </section>
  );
};

export default Home;
