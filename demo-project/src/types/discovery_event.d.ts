/* eslint-disable */
/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */

/**
 * Pytest Discover Event
 */
export type DiscoveryEvent =
  | CollectReport
  | ErrorMessage
  | WarningMessage
  | SessionStart
  | SessionFinish

/**
 * Pytest Collect Report
 */
export interface CollectReport {
  /**
   * The event type
   */
  event: "CollectReport"
  /**
   * The node id of the collector (if any)
   */
  node_id: string
  /**
   * The collected items
   */
  items: (TestDirectory | TestModule | TestSuite | TestCase)[]
  [k: string]: unknown
}
/**
 * Pytest Test Directory
 */
export interface TestDirectory {
  /**
   * Node ID
   */
  node_id: string
  /**
   * Node Type
   */
  node_type: "directory"
  /**
   * Test Name
   */
  name: string
  /**
   * Directory path
   */
  path: string
  [k: string]: unknown
}
/**
 * Pytest Test Module
 */
export interface TestModule {
  /**
   * Node ID
   */
  node_id: string
  /**
   * Node Type
   */
  node_type: "module"
  /**
   * Module name
   */
  name: string
  /**
   * File path
   */
  path: string
  /**
   * Module docstring
   */
  doc: string
  /**
   * Test markers
   */
  markers: string[]
  [k: string]: unknown
}
/**
 * Pytest Test Suite
 */
export interface TestSuite {
  /**
   * Node ID
   */
  node_id: string
  /**
   * Node Type
   */
  node_type: "suite"
  /**
   * Suite name
   */
  name: string
  /**
   * Module name
   */
  module: string
  /**
   * File path
   */
  path: string
  /**
   * Suite documentation
   */
  doc: string
  /**
   * Test markers
   */
  markers: string[]
  [k: string]: unknown
}
/**
 * Pytest Test Case
 */
export interface TestCase {
  /**
   * Node ID
   */
  node_id: string
  /**
   * Node Type
   */
  node_type: "case"
  /**
   * File path
   */
  path: string
  /**
   * Module name
   */
  module?: string
  /**
   * Parent suite
   */
  suite?: string
  /**
   * Function name
   */
  function?: string
  /**
   * Test Name
   */
  name: string
  /**
   * Test docstring
   */
  doc: string
  /**
   * Test markers
   */
  markers: string[]
  /**
   * Test parameters names and types
   */
  parameters: {
    [k: string]: string
  }
  [k: string]: unknown
}
/**
 * An error message
 */
export interface ErrorMessage {
  /**
   * The event type
   */
  event: "ErrorMessage"
  /**
   * When the error message is emitted
   */
  when: "config" | "collect" | "runtest"
  location: Location
  /**
   * The exception type
   */
  exception_type: string
  /**
   * The exception value
   */
  exception_value: string
  traceback: Traceback
  [k: string]: unknown
}
/**
 * The location of the error
 */
export interface Location {
  /**
   * File name
   */
  filename: string
  /**
   * Line number
   */
  lineno: number
  [k: string]: unknown
}
/**
 * The traceback of the error
 */
export interface Traceback {
  /**
   * Traceback entries
   */
  lines: string[]
  [k: string]: unknown
}
/**
 * A warning message
 */
export interface WarningMessage {
  /**
   * The event type
   */
  event: "WarningMessage"
  /**
   * When the warning message is emitted
   */
  when: "config" | "collect" | "runtest"
  /**
   * The node ID of the node where the warning message is emitted
   */
  node_id: string
  location: Location1
  /**
   * The warning message
   */
  message: string
  /**
   * The category of the warning message
   */
  category?: string
  [k: string]: unknown
}
/**
 * Location in code source
 */
export interface Location1 {
  /**
   * File name
   */
  filename: string
  /**
   * Line number
   */
  lineno: number
  [k: string]: unknown
}
/**
 * Pytest Session Start
 */
export interface SessionStart {
  /**
   * The event type
   */
  event: "SessionStart"
  /**
   * The version of pytest that is running the tests
   */
  pytest_version: string
  /**
   * The version of pytest-discover plugin that discovered the tests
   */
  plugin_version: string
  [k: string]: unknown
}
/**
 * Pytest Session Finish
 */
export interface SessionFinish {
  /**
   * The event type
   */
  event: "SessionFinish"
  /**
   * The status which pytest will return to the system
   */
  exit_status: number
  [k: string]: unknown
}
