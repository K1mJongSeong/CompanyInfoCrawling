"use client";

import PaginationBox from "@/components/common/Pagination";
import NoSearch from "@/components/search/NoSearch";
import SearchList, { SearchItem } from "@/components/search/SearchList";
import SearchTop from "@/components/search/SearchTop";
import { SearchCard, SearchLayoutContainer } from "@/components/search/styles";
import { useAuth } from "@/contexts/auth.context";
import { Stack, Typography } from "@mui/material";
import { useSnackbar } from "notistack";
import { useEffect, useState } from "react";
interface Props {
  slug: Array<string>;
}
export default function SearchContainer({ slug }: Props) {
  const [searchValue, setSearchValue] = useState<string>("");
  useEffect(() => {
    if (slug) {
      setSearchValue(decodeURI(decodeURIComponent(slug[0])));
    } else {
      setSearchValue("");
    }
  }, [slug]);

  const { user } = useAuth();
  const { enqueueSnackbar } = useSnackbar();

  const [result, setResult] = useState(true);

  const handleClickItem = async () => {
    if (!user) {
      enqueueSnackbar("Only members can use it", { variant: "warning" });
      return false;
    } else {
      return true;
    }
  };
  return (
    <SearchLayoutContainer>
      <SearchTop searchValue={searchValue} />
      <SearchCard>
        <Stack direction={"row"} mb={3} gap={1} alignItems={"flex-end"}>
          <Typography variant="h2" fontSize={"large"} fontWeight={"bold"}>
            {searchValue}
          </Typography>
          <Typography variant="body1" fontSize={"small"}>
            Search Reasult 0000
          </Typography>
        </Stack>
        {result ? (
          <>
            <SearchList>
              <SearchItem onClick={handleClickItem} />
              <SearchItem onClick={handleClickItem} />
              <SearchItem onClick={handleClickItem} />
              <SearchItem onClick={handleClickItem} />
              <SearchItem onClick={handleClickItem} />
              <SearchItem onClick={handleClickItem} />
              <SearchItem onClick={handleClickItem} />
              <SearchItem onClick={handleClickItem} />
              <SearchItem onClick={handleClickItem} />
              <SearchItem onClick={handleClickItem} />
              <SearchItem onClick={handleClickItem} />
            </SearchList>
            <PaginationBox />
          </>
        ) : (
          <NoSearch />
        )}
      </SearchCard>
    </SearchLayoutContainer>
  );
}
