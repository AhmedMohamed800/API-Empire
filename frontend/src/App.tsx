import Auth from "./layouts/Auth.tsx";
import Application from "./layouts/Application.tsx";
import Signin from "./pages/Signin.tsx";
import Signup from "./pages/Signup.tsx";
import ForgetPassword from "./pages/ForgetPassword.tsx";
import APIs from "./pages/APIs.tsx";
import User from "./pages/User.tsx";
import React from "react";
import Billing from "./pages/Billing.tsx";
import Traffic from "./pages/Traffic.tsx";
import API from "./pages/API.tsx";
import ResetPassowrd from "./pages/ResetPassowrd.tsx";
import { Route, Routes } from "react-router-dom";

const App = () => {
  return (
    <Routes>
      <Route element={<Auth />}>
        <Route path="/auth/sign_in" element={<Signin />} />
        <Route path="/auth/sign_up" element={<Signup />} />
        <Route path="/auth/forget" element={<ForgetPassword />} />
        <Route path="/auth/reset/:token" element={<ResetPassowrd />} />
      </Route>
      <Route element={<Application />}>
        <Route path="/APIs" element={<APIs />} />
        <Route path="/API/:id" element={<API />} />
        <Route path="/user" element={<User />} />
        <Route path="/billing" element={<Billing />} />
        <Route path="/traffic" element={<Traffic />} />
      </Route>
    </Routes>
  );
};

export default App;
