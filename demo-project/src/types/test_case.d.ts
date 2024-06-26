/* eslint-disable */
/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */

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
