import React from "react";
import { Outlet } from "react-router-dom";
import NavbarApp from "../components/Application/NavbarApp.tsx";
import Footer from "../components/Application/Footer.tsx";

const Application = () => {
  return (
    <section className="px-20">
      <NavbarApp />
      <Outlet />
      <Footer />
    </section>
  );
};

export default Application;
