<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="4.0">
    
    <xsl:output method="text" indent="yes"/>
    
    
    <xsl:template match="/">
        
        
        <xsl:apply-templates select="//list"/>
        
        
    </xsl:template>
    
    <xsl:template match="list">
        
        <xsl:apply-templates select="distinct-values(descendant::artist)" separator="&#x9;"/> />
        <xsl:value-of select="count(distinct-values(//artist))" separator="&#xa;"/>
    </xsl:template>
    
</xsl:stylesheet>