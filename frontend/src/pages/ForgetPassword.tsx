import React from "react";
import Label from "../components/Auth/Label.tsx";
const logo = require("../assets/logo.svg") as string;
const cover = require("../assets/auth/cover.svg") as string;
import { useFormForget } from "../components/Auth/AuthHook.tsx";
import { Link } from "react-router-dom";

const ForgetPassword = () => {
  const { form, handleForm, submitForm } = useFormForget();
  return (
    <section className="flex w-[50%] flex-col items-center justify-center gap-10 bg-background px-20 pt-[55px] max-lg:w-[100%] max-sm:px-5">
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
          <h1 className="text-2xl font-extrabold">Forget Password</h1>
        </div>
        <Label
          id="email"
          type="email"
          placeholder="Enter your email"
          name="Email"
          handle={handleForm}
          value={form.email}
        />
        <button className="mt-6 rounded-md bg-primary py-3 font-bold text-white hover:opacity-80">
          Send Email
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
};

export default ForgetPassword;
