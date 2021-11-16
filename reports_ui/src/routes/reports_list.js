import React, { useState, useEffect } from "react";
import {
  Outlet,
  useSearchParams,
  useLocation
} from "react-router-dom";

import "../css/style.css"
import QueryNavLink from "../components/QueryNavLink";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faFilter } from '@fortawesome/free-solid-svg-icons'


export default function ReportList() {
  const [reports, setReports] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchParams, setSearchParams] = useSearchParams();

  let location = useLocation();
  let reportPath = location.pathname.slice(1).split("/")[0]

  useEffect(() => {
    fetch(`http://172.20.0.4:5000/report/${reportPath}`)
    .then((response) => {
      if (response.ok) {
        return response.json();
      }
      throw response;
    })
    .then(reports => setReports(reports))
    .catch((error) => {
      console.error("Error fetching reports: ", error);
      setError(error);
    })
    .finally(() => {
      setLoading(false);
    });
  }, [reportPath]);

  if (loading) return "Loading...";
  if (error) return "Error!";

  return (
    <div style={{ display: "flex" }}>
      <nav
        style={{
          borderRight: "solid 1px",
          padding: "1rem"
        }}
      >
        <div className="search-bar">  
          <FontAwesomeIcon icon={faFilter} size="sm" />
          <input
            value={searchParams.get("filter") || ""}
            onChange={event => {
              let filter = event.target.value;
              if (filter) {
                setSearchParams({ filter });
              } else {
                setSearchParams({});
              }
            }}
            className="search-bar-input"
          />
        </div>

        {reports
          .filter(report => {
            let filter = searchParams.get("filter");
            if (!filter) return true;
            let year_month = `${report.reference_year}${report.reference_month}`
            return year_month.startsWith(filter);
          })
          .map(report => {
            return (
              <QueryNavLink
                className={({ isActive }) => isActive ? "report-link active" : "report-link gray"}
                to={`/${reportPath}/${report._id}`}
                key={report._id}
              >
                {report.reference_year}-
                {report.reference_month}
              </QueryNavLink>
            )
          })
        }
      </nav>
      <Outlet />
    </div>
  );
}