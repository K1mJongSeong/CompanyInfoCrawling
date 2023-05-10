import { Box, Stack } from "@mui/material";
import styled from "@emotion/styled";

export const SearchLayoutContainer = styled(Box)`
  max-width: 1586px;
  display: flex;
  flex-direction: column;
  height: max-content;
  margin: 0 auto;
  gap: 65px;
  padding-bottom: 100px;
`;

export const SearchTopBgBox = styled(Box)`
  width: 100%;
  height: 80px;
  border-radius: 0 0 80px 80px;
  /* Permalink - use to edit and share this gradient: https://colorzilla.com/gradient-editor/#5b7fff+0,7654ff+100 */
  background: #5b7fff; /* Old browsers */
  background: -moz-linear-gradient(
    -45deg,
    #5b7fff 0%,
    #7654ff 100%
  ); /* FF3.6-15 */
  background: -webkit-linear-gradient(
    -45deg,
    #5b7fff 0%,
    #7654ff 100%
  ); /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(
    135deg,
    #5b7fff 0%,
    #7654ff 100%
  ); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#5b7fff', endColorstr='#7654ff',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
`;

export const SearchCard = styled(Box)`
  width: calc(100% - 32px);
  max-width: 1388px;
  background-color: white;
  border-radius: 8px;
  margin: 0 auto;
  box-shadow: 4px 4px 20px rgba(23, 33, 122, 0.3);
  padding: 25px 1rem 56px;
`;
