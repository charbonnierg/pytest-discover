import SlCard from "@shoelace-style/shoelace/dist/react/card/index.js"

import { getFilename, sanitizeName } from "../../../../lib/files.ts"
import type { TestCase } from "../../../../types/test_case"
import { CopyBadge } from "../../../widgets/copy-badge/CopyBadge.tsx"
import { MarkersList } from "../markers-list/MarkersList.tsx"
import "./TestItemCard.css"

interface TestItemCardProps {
  onClick: (props: TestCase) => void
  properties: TestCase
}

/* A test item collected by pytest */
export const TestItemCard = (item: TestItemCardProps) => {
  return (
    <SlCard
      key={item.properties.node_id}
      className="test-item-card"
      onClick={() => {
        item.onClick(item.properties)
      }}
    >
      <h3>{sanitizeName(item.properties.name)}</h3>
      <MarkersList item={item.properties} />
      <p>
        <CopyBadge
          label={getFilename(item.properties.path)}
          value={item.properties.path}
          icon="filetype-py"
        />
      </p>
      {truncateDescription(item.properties.doc)}
    </SlCard>
  )
}

/* Format a test item docstring */
const truncateDescription = (doc: string | null): string => {
  if (doc == null || doc == "") {
    return ""
  }
  if (doc.length > 100) {
    return doc.slice(0, 100) + "..."
  }
  return doc
}

export default TestItemCard
