import React from "react";
import { Link } from "react-router-dom";
import Label from "../components/Auth/Label.tsx";
const logo = require("../assets/logo.svg") as string;
const cover = require("../assets/auth/cover.svg") as string;
import { useFormIN } from "../components/Auth/AuthHook.tsx";

function Signin() {
  const { form, error, handleForm, submitForm } = useFormIN();
  return (
    <section className="flex w-[50%] flex-col items-center gap-10 bg-background px-20 pt-[55px] max-lg:w-[100%] max-sm:px-5">
      <article className="flex flex-col items-center justify-center gap-1 font-semibold">
        <h1 className="flex items-center gap-1 text-2xl  text-white">
          <span>
            <img src={logo} alt="logo" width="43.39px" height="32px" />
          </span>
          API EMPIRE
        </h1>
        <p className="text-md text-neutral-400">
          Unleash the Power of Connectivity
        </p>
      </article>
      <form
        onSubmit={submitForm}
        className="relative z-10 flex w-full flex-col rounded-md border border-white bg-black p-8"
      >
        <div className="mb-6 text-white">
          <h1 className="text-2xl font-extrabold">Sign In</h1>
          <p className="text-md font-semibold">
            New user?{" "}
            <Link
              to="/auth/sign_up"
              className=" border-b-2 border-primary text-primary hover:opacity-80"
            >
              Create an account
            </Link>
          </p>
        </div>
        <div className="flex flex-col gap-6">
          <Label
            id="email"
            type="email"
            placeholder="Enter your email"
            name="Email"
            handle={handleForm}
            value={form.email}
          />
          <Label
            id="password"
            type="password"
            placeholder="Enter your password"
            name="Password"
            handle={handleForm}
            value={form.password}
          />
        </div>
        <p className="text-red-500">{error}</p>
        <div className="my-3 flex flex-row-reverse justify-between gap-2 max-sm:flex-col-reverse">
          <Link
            to="/auth/forget"
            className=" w-fit text-sm font-bold text-primary hover:opacity-80"
          >
            Forgot your password?
          </Link>
          <Label
            id="remember"
            type="checkbox"
            name="Remember me"
            handle={handleForm}
            value={form.remember_me}
          />
        </div>

        <button className="mt-6 rounded-md bg-primary py-3 font-bold text-white hover:opacity-80">
          Sign In
        </button>

        <img
          src={cover}
          alt="cover"
          width="44.88px"
          height="74px"
          className=" absolute right-0 top-0"
        />
      </form>

      <div className=" absolute -right-10 bottom-0  h-56 w-56 rounded-full bg-primary blur-[160px]"></div>
    </section>
  );
}

export default Signin;
