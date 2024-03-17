import React from "react";
import { Outlet } from "react-router-dom";
import NavbarApp from "../components/Application/NavbarApp.tsx";
import Footer from "../components/Application/Footer.tsx";
import { useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import { UserContext } from "../components/Auth/AuthHook.tsx";
import Cookies from "js-cookie";

interface User {
  email: string;
  first_name: string;
  last_name: string;
  api_key: string;
}

interface UserContextType {
  user: User;
  setUser: React.Dispatch<React.SetStateAction<User>>;
}

const Application = () => {
  const navigate = useNavigate();
  const [user, setUser] = useState<User>({
    email: "",
    first_name: "",
    last_name: "",
    api_key: "",
  });

  useEffect(() => {
    const LOGINURL = `${process.env.REACT_APP_API_URL}/api/v1/user`;
    let session_id = Cookies.get("session");
    if (session_id) {
      axios
        .get(LOGINURL, {
          headers: {
            "session-id": JSON.parse(session_id),
          },
        })
        .then((response) => {
          const { email, first_name, last_name, api_key } = response.data;
          setUser({ email, first_name, last_name, api_key });
        })
        .catch((error) => {
          console.error(error);
          Cookies.remove("session");
          navigate("/auth/sign_in");
        });
    } else {
      navigate("/auth/sign_in");
    }
  }, []);

  return (
    <UserContext.Provider value={{ user, setUser } as UserContextType}>
      <section className=" relative flex max-h-full min-h-screen flex-col justify-between  text-white [&>*:nth-child(2)]:flex-grow">
        <NavbarApp />
        <Outlet />
        <Footer />
        <div className=" absolute -right-10 bottom-0 h-56 w-56 rounded-full bg-primary blur-[160px]"></div>
        <div className=" absolute -left-10 top-0    h-56 w-56 rounded-full bg-primary blur-[160px]"></div>
      </section>
    </UserContext.Provider>
  );
};

export default Application;
