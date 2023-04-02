import React, { useEffect, useState } from "react";
import axios from "axios";
export const ApiLogin = () => {
  const [Data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/books").then((response) => {
      console.log(response);
    });
  }, []);

  return <>ApiLogin</>;
};
