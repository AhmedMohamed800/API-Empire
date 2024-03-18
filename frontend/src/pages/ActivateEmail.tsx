import React from "react";
import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "axios";

type Props = {};

const ActivateEmail = (props: Props) => {
  const { token } = useParams();
  const navigate = useNavigate();
  const [error, setError] = useState<boolean>(false);

  useEffect(() => {
    const ACTIVATEURL = `${process.env.REACT_APP_API_URL}/api/v1/user`;
    console.log(ACTIVATEURL);
    axios
      .post(ACTIVATEURL, {}, { headers: { token } })
      .then((res) => {
        navigate("/auth/sign_in");
      })
      .catch((error) => {
        setError(true);
        console.log(error);
      });
  }, []);

  return (
    <div className="flex flex-col items-center justify-center gap-5 text-5xl font-semibold">
      {error || (
        <>
          <h1>Thank you for activating your email</h1>
          <h2 className="loading-indicator">Redirecting to login page</h2>
        </>
      )}
      {error && (
        <p className="text-center">
          Error activating your email, please try again
        </p>
      )}
    </div>
  );
};

export default ActivateEmail;
