"use client";
import { styled } from "@mui/material/styles";
import ArrowForwardIosSharpIcon from "@mui/icons-material/ArrowForwardIosSharp";
import MuiAccordion, { AccordionProps } from "@mui/material/Accordion";
import MuiAccordionSummary, {
  AccordionSummaryProps,
} from "@mui/material/AccordionSummary";
import MuiAccordionDetails from "@mui/material/AccordionDetails";
import Typography from "@mui/material/Typography";
import { useEffect, useState } from "react";
import { Stack, useMediaQuery, useTheme } from "@mui/material";
import uuid from "react-uuid";
import { grey } from "@mui/material/colors";

const Accordion = styled((props: AccordionProps) => (
  <MuiAccordion disableGutters elevation={0} square {...props} />
))(({ theme }) => ({
  border: `1px solid ${theme.palette.divider}`,
  "&:not(:last-child)": {},
  "&:before": {
    display: "none",
  },
}));

const AccordionSummary = styled((props: AccordionSummaryProps) => (
  <MuiAccordionSummary
    expandIcon={<ArrowForwardIosSharpIcon sx={{ fontSize: "0.9rem" }} />}
    {...props}
  />
))(({ theme }) => ({
  fontSize: "18px",
  fontWeight: "bold",
  color: "#73767C",
  "& .MuiAccordionSummary-expandIconWrapper.Mui-expanded": {
    transform: "rotate(90deg)",
  },
  "& .MuiAccordionSummary-content": {
    marginRight: theme.spacing(1),
    alignItems: "center",
    flexWrap: "wrap",
    gap: 8,
  },
  "& .MuiAccordionSummary-content.Mui-expanded": {
    color: "#17217A",
  },
}));

const AccordionDetails = styled(MuiAccordionDetails)(({ theme }) => ({
  padding: theme.spacing(2),
}));

export default function CustomizedAccordions({ data }: { data: Array<any> }) {
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.up("md"));
  const [expanded, setExpanded] = useState<string | false>("panel0");

  const handleChange =
    (panel: string) => (event: React.SyntheticEvent, newExpanded: boolean) => {
      setExpanded(newExpanded ? panel : false);
    };

  const [mounted, setMounted] = useState<boolean>(false);
  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) {
    return <>Loading...</>;
  }
  console.log(data);

  return (
    <Stack direction={"column"} gap={1} px={matches ? 5 : 0}>
      {mounted &&
        data.map((el, idx) => (
          <Accordion
            key={uuid()}
            expanded={expanded === `panel${idx}`}
            onChange={handleChange(`panel${idx}`)}
          >
            <AccordionSummary
              aria-controls={`panel${idx}-content`}
              id={`panel${idx}-header`}
            >
              <Typography fontWeight={"bold"}>{el.question}</Typography>
              <Typography fontSize={12} color={grey[500]}>
                {el.question_content}
              </Typography>
            </AccordionSummary>
            <AccordionDetails>
              <Typography fontSize={14}>{el.answer}</Typography>
            </AccordionDetails>
          </Accordion>
        ))}
    </Stack>
  );
}
