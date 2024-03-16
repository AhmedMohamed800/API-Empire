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
import Home from "./layouts/Home.tsx";
import LandingPage from "./pages/LandingPage.tsx";
import Aboutus from "./pages/Aboutus.tsx";
import Pricing from "./pages/Pricing.tsx";
import NotFound from "./pages/NotFound.tsx";
import { PayPalScriptProvider } from "@paypal/react-paypal-js";

const App = () => {
  const initialOptions = {
    clientId:
      "Acc2NHlsRMBVgXGafvkkkvd1QFCRV4HOAPRqfysiLrGYRu_lyKTHDcl4aGbe3zyDe7YG9yd9K2jsv0qe",
    currency: "USD",
    intent: "capture",
  };

  return (
    <PayPalScriptProvider options={initialOptions}>
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
        <Route element={<Home />}>
          <Route path="/" index element={<LandingPage />} />
          <Route path="/aboutus" element={<Aboutus />} />
          <Route path="/pricing" element={<Pricing />} />
          <Route path="/apihub" element={<APIs />} />
          <Route path="/apihub/:id" element={<API />} />
        </Route>
        <Route path="*" element={<NotFound />} />
      </Routes>
    </PayPalScriptProvider>
  );
};

export default App;
