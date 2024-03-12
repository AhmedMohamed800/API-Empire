import Auth from "./layouts/Auth.tsx";
import Signin from "./pages/Signin.tsx";
import Signup from "./pages/Signup.tsx";
import React from "react";
import { Route, Routes } from "react-router-dom";

const App = () => {
  return (
    <Routes>
      <Route element={<Auth />}>
        <Route path="/auth/sign_in" element={<Signin />} />
        <Route path="/auth/sign_up" element={<Signup />} />
        <Route path="/" element={<Signup />} />
      </Route>
    </Routes>
  );
};

export default App;
