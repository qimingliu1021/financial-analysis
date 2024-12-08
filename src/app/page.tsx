"use client";
import Image from "next/image";
import React, { useEffect, useState } from "react";

export default function Home() {
  const [data, setData] = useState(null);
  const testFetchData = async () => {
    try {
      const response = await fetch("http://localhost:8000/auto_research");
      const data = await response.json();
      setData(data);
      console.log(data);
    } catch (error) {
      console.error("Error fetching data: ", error);
    }
  };

  useEffect(() => {
    testFetchData();
  }, []);

  return (
    <div>
      <h1>Fetched data: </h1>
      {data ? <pre>{JSON.stringify(data, null, 2)}</pre> : <p>Loading...</p>}
    </div>
  );
}
