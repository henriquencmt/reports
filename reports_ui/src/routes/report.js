import React, {
  useState,
  useEffect } from "react";
import { useParams, useLocation } from "react-router-dom"

import DownloadPptBtn from "../components/DownloadPptBtn";
import DownloadXlBtn from "../components/DownloadXlBtn";
import "../css/style.css"


export default function Report() {
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const params = useParams();

  let location = useLocation();
  let reportPath = location.pathname.slice(1).split("/")[0]

  useEffect(() => {
    fetch(`http://172.20.0.4:5000/report/${reportPath}/?id=${params.reportId}`)
      .then((res) => {
        if (res.ok) {
          return res.json();
        }
        throw res;
      })
      .then(data => setReport(data))
      .catch((error) => {
        console.error("Error fetching reports: ", error);
        setError(error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, [reportPath, params.reportId]);

  if (loading) return "Loading...";
  if (error) return "Error!";

  return (
    <main style={{ padding: "1rem" }}>
      <h2>{reportPath} {report.reference_year}-{report.reference_month}</h2>
      <p>ID: {report._id}</p>

      <DownloadXlBtn />
      <DownloadPptBtn />
    </main>
  );
}