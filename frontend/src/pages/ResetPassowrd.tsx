import React from "react";
import { useParams } from "react-router-dom";
import { useEffect } from "react";
const cover = require("../assets/auth/cover.svg") as string;
const logo = require("../assets/logo.svg") as string;
import { useFromReset } from "../components/Auth/AuthHook.tsx";
import Label from "../components/Auth/Label.tsx";

const ResetPassowrd = () => {
  const { token } = useParams();
  const { form, handleForm, submitForm, setForm, error } = useFromReset();

  useEffect(() => {
    setForm((prevState) => ({
      ...prevState,
      token: token,
    }));
  }, []);

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
          <h1 className="text-2xl font-extrabold">Reset Password</h1>
        </div>
        <div className="flex flex-col gap-6">
          <Label
            id="password"
            type="password"
            placeholder="Enter your new password"
            name="Password"
            handle={handleForm}
            value={form.password}
          />
          <Label
            id="passwordConfirm"
            type="password"
            placeholder="Enter your new password"
            name="Confirm password"
            handle={handleForm}
            value={form.passwordConfirm}
          />
        </div>
        <p className="text-red-500">{error}</p>

        <button className="mt-6 rounded-md bg-primary py-3 font-bold text-white hover:opacity-80">
          Reset Password
        </button>
        <img
          src={cover}
          alt="cover"
          width="44.88px"
          height="74px"
          className=" absolute right-0 top-0"
        />
      </form>
    </section>
  );
};

export default ResetPassowrd;
