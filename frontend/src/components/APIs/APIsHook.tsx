import { useState, useEffect, useRef, useMemo } from "react";
import axios from "axios";
import APICard from "./APICard.tsx";
import React from "react";

interface APICardProps {
  title: string;
  description: string;
  image_cover: string;
  id: string;
  category: string;
}

export const usePaginatedAPIs = (apisPerPage) => {
  const [apis, setApis] = useState([]);
  const [filteredApis, setFilteredApis] = useState<number>(1);
  const [page, setPage] = useState(1);
  const [searchTerm, setSearchTerm] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("");
  const [Categories, setCategories] = useState([]);
  const topRef = useRef(null);

  const paginate = (pageNumber) => {
    setPage(pageNumber);
    const url = new URL(window.location.href);
    url.searchParams.set("page", pageNumber);
    window.history.replaceState({}, "", url);
  };

  useEffect(() => {
    const url = new URL(window.location.href);
    const page = url.searchParams.get("page");
    if (page) {
      setPage(parseInt(page));
    } else {
      paginate(1);
    }
    document.title = "APIs";
    const APIsURL = `${process.env.REACT_APP_API_URL}/api/v1/service/all`;

    axios
      .get(APIsURL)
      .then((response) => {
        setApis(response.data.service);
        setCategories(response.data.categorys);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  const computedApis = useMemo(() => {
    let filteredApis: APICardProps[] = apis;
    if (searchTerm) {
      filteredApis = filteredApis.filter((api: APICardProps) =>
        api.title.toLowerCase().includes(searchTerm.toLowerCase()),
      );
    }
    if (selectedCategory) {
      filteredApis = filteredApis.filter(
        (api: APICardProps) => api.category === selectedCategory,
      );
    }
    setFilteredApis(filteredApis.length);
    const startIndex = (page - 1) * apisPerPage;
    const endIndex = startIndex + apisPerPage;
    return filteredApis.slice(startIndex, endIndex).map((api: APICardProps) => {
      return (
        <APICard
          key={api.id}
          title={api.title}
          description={api.description}
          image_cover={api.image_cover}
          url={api.id}
          category={api.category}
        />
      );
    });
  }, [apis, page, searchTerm, selectedCategory]);

  function generateUUID() {
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(
      /[xy]/g,
      function (c) {
        var r = (Math.random() * 16) | 0,
          v = c === "x" ? r : (r & 0x3) | 0x8;
        return v.toString(16);
      },
    );
  }

  return {
    computedApis,
    paginate,
    topRef,
    page,
    filteredApis,
    generateUUID,
    setSearchTerm,
    setSelectedCategory,
    selectedCategory,
    searchTerm,
    Categories,
  };
};
