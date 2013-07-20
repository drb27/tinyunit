<?xml version="1.0" ?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
    <html>
    <head>
    <link rel='stylesheet' type='text/css' href='results.css' media='screen'/>
    </head>
    <body>
    <h2> Test Results</h2>
    <xsl:for-each select="testrun/testcase">
        <div>
        <p>
            Results for test case <b><xsl:value-of select="@name"/></b>:
        </p>
        <table border="1">
            <th>Method</th><th>Result</th>
            <xsl:for-each select="method">
            <tr>
                <td><xsl:value-of select="name"/></td>
                <xsl:choose>
                <xsl:when test="result='fail'">
                    <td bgcolor="#ff0000"><xsl:value-of select="result"/></td>
                </xsl:when>
                <xsl:when test="result='error'">
                    <td bgcolor="#ffff00"><xsl:value-of select="result"/></td>
                </xsl:when>
                <xsl:otherwise>
                    <td bgcolor="#00ff00"><xsl:value-of select="result"/></td>
                </xsl:otherwise>
                </xsl:choose>
                
            </tr>
            </xsl:for-each>
        </table>
        </div>
    </xsl:for-each>
    <p>One day, a summary of the results may appear here</p>
    </body>
    </html>
</xsl:template>
</xsl:stylesheet>

