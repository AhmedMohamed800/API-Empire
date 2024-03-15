import React from "react";
import { useEffect } from "react";
import axios from "axios";
import Cookies from "js-cookie";

const User = () => {
  useEffect(() => {
    const session_id = Cookies.get("session");
    const KEYURL = `${process.env.REACT_APP_API_URL}/api/v1/get_key`;
    axios
      .post(KEYURL, { "session-id": JSON.parse(session_id) })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  });

  return <div>User</div>;
};

export default User;
