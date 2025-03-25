<p:declare-step xmlns:p="http://www.w3.org/ns/xproc" exclude-inline-prefixes="#all"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:ex="extensions"
    xmlns:cx="http://xmlcalabash.com/ns/extensions" xmlns:c="http://www.w3.org/ns/xproc-step"
    version="3.0">
    <p:input port="source" primary="true" href="movieData-short.txt" sequence="false"/>
    <p:output port="result" primary="true" sequence="true"/>
    
    <p:invisible-xml>
        <p:with-input port="grammar">
            <p:document href="movieDataSolution.ixml" content-type="text/plain"/>
        </p:with-input>
    <p:identity/>
</p:declare-step>